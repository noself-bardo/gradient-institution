/**
 * TG-WEB-001 — The Gradient Archive Gateway
 * Plate Reader — Public Field Atlas
 */

const esc = (s) => String(s)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;")
  .replaceAll("'", "&#039;");

async function loadJSON(path) {
  const res = await fetch(path);
  if (!res.ok) throw new Error(`Failed to load ${path}`);
  return res.json();
}

async function probePdf(path) {
  try {
    const res = await fetch(path, { method: "HEAD" });
    return res.ok;
  } catch {
    return false;
  }
}

async function buildAvailabilityMap(paths) {
  const unique = [...new Set(paths.filter(Boolean))];
  const entries = await Promise.all(unique.map(async (path) => [path, await probePdf(path)]));
  return Object.fromEntries(entries);
}

function collectPdfPaths(governing, companion, modules, readerPath) {
  const paths = [];
  governing.forEach((item) => paths.push(item.pdf));
  companion.forEach((item) => paths.push(item.pdf));
  modules.forEach((item) => paths.push(item.sourceAction?.pdf));
  readerPath.forEach((item) => paths.push(item.pdf));
  return paths;
}

function pdfAction(item, availability, labelOverride) {
  const label = labelOverride || item.actionLabel || "OPEN DOCUMENT (PDF)";
  const path = item.pdf || item;
  const available = typeof path === "string" ? availability[path] : availability[item.pdf];

  if (available) {
    const href = typeof path === "string" ? path : item.pdf;
    return `<a class="act" href="${esc(href)}" target="_blank" rel="noopener noreferrer"><span class="mark"></span>${esc(label)}</a>`;
  }

  return `<span class="act pending" aria-disabled="true"><span class="mark"></span>READER PDF NEEDED</span>`;
}

function companionDetailLines(item) {
  const fields = [
    ["RANGE", item.range],
    ["WEB AVAILABILITY", item.webAvailability],
    ["READER STATUS", item.readerStatus],
    ["PDF STATUS", item.pdfStatus],
    ["ARCHIVE NOTE", item.archiveNote],
    ["BOUNDARY NOTE", item.boundaryNote],
    ["SOURCE NOTE", item.sourceNote]
  ];

  return fields
    .filter(([, value]) => value)
    .map(([label, value]) => `<div style="margin-top:8px;">${label}: ${esc(value)}</div>`)
    .join("");
}

function renderLedger(targetId, items, availability) {
  const el = document.getElementById(targetId);
  if (!el) return;

  el.innerHTML = items.map((it) => {
    const available = availability[it.pdf];
    const statusLine = available ? "AVAILABLE" : "PENDING — READER PDF NEEDED";

    return `
    <div class="entry">
      <div class="entryTop">
        <div>ACC: ${esc(it.acc || "—")}</div>
        <div>${it.authority ? `AUTH: ${esc(it.authority)}` : ""}</div>
      </div>
      <div class="entryTitle">${esc(it.title)}</div>
      <div class="entryBody">
        <div>STATUS: ${esc(it.status || "—")}</div>
        <div style="margin-top:8px;">ROLE: ${esc(it.usedFor || "—")}</div>
        <div style="margin-top:8px;">FORMAT: PDF / PLATE LANGUAGE</div>
        <div style="margin-top:8px;">ACCESS: ${esc(statusLine)}</div>
        ${companionDetailLines(it)}
      </div>
      <div class="entryActions">
        ${pdfAction(it, availability)}
      </div>
    </div>`;
  }).join("");
}

function renderArtifacts(items) {
  const host = document.getElementById("artifactGrid");
  if (!host) return;

  host.innerHTML = items.map((a) => {
    const phId = esc(a.src).replace(/\W/g, "-");
    return `
    <div class="artifact">
      <div class="artifactPlaceholder" id="ph-${phId}">ARTIFACT PLATE / IMAGE PENDING</div>
      <img class="artifactImg" src="${esc(a.src)}" alt="${esc(a.alt)}"
        onerror="this.classList.add('missing'); document.getElementById('ph-${phId}')?.classList.add('visible');" />
      <div class="artifactCap">
        <span>${esc(a.capLeft)}</span>
        <span>${esc(a.capRight)}</span>
      </div>
      <div class="artifactNote">COMPANION SOURCE / VISUAL RHYTHM ONLY / NOT AUTHORITY</div>
    </div>`;
  }).join("");
}

function renderModulePlates(modules, availability) {
  const host = document.getElementById("modulePlates");
  if (!host) return;

  host.innerHTML = modules.map((m) => `
    <div class="modulePlate">
      <div class="moduleHead">
        <div>${esc(m.id)} / ${esc(m.short)}</div>
        <div>SOURCE STATUS: GOVERNING</div>
      </div>
      <div class="moduleName">${esc(m.id)} / ${esc(m.short)}</div>
      <div class="moduleTriptych">
        <div class="lineItem">
          <div class="lineLbl">QUOTE (VERBATIM)</div>
          <div class="lineVal">"${esc(m.quote)}"</div>
        </div>
        <div class="lineItem">
          <div class="lineLbl">INTERPRETATION (LABELED)</div>
          <div class="lineVal">${esc(m.interpretation)}</div>
        </div>
        <div class="lineItem">
          <div class="lineLbl">READER INSTRUCTION</div>
          <div class="lineVal">${esc(m.readerInstruction)}</div>
        </div>
      </div>
      <div class="entryActions" style="margin-top:14px;">
        <button type="button" class="act" data-open-module="${esc(m.id)}"><span class="mark"></span>OPEN MODULE (LOCAL)</button>
        ${pdfAction({ pdf: m.sourceAction.pdf, actionLabel: m.sourceAction.label }, availability)}
      </div>
      <div class="metaBlock" style="margin-top:16px;">
        <div class="metaItem">TITLE: <strong>${esc(m.title)}</strong></div>
        <div class="metaItem">READ NEXT: <strong>${esc(m.modal.readNext)}</strong></div>
        <div class="metaItem">STATUS: <strong>READY</strong></div>
        <div class="metaItem">ACCESSION: <strong>${esc(m.id)}-PLATE</strong></div>
      </div>
    </div>
  `).join("");
}

function renderReaderPath(items, availability) {
  const host = document.getElementById("readerPathActions");
  if (!host) return;

  host.innerHTML = items.map((item) =>
    pdfAction({ pdf: item.pdf, actionLabel: item.label }, availability)
  ).join("");
}

function renderFooter(meta) {
  const host = document.getElementById("footerAccession");
  if (!host || !meta) return;

  host.innerHTML = `
    <div class="accLine"><div class="accKey">ASSET ID:</div><div class="accVal">${esc(meta.assetId)}</div></div>
    <div class="accLine"><div class="accKey">TITLE:</div><div class="accVal">${esc(meta.title)}</div></div>
    <div class="accLine"><div class="accKey">AUTHORITY LAYER:</div><div class="accVal">${esc(meta.authorityLayer)}</div></div>
    <div class="accLine"><div class="accKey">STATUS:</div><div class="accVal">${esc(meta.status)}</div></div>
    <div class="accLine"><div class="accKey">BOUNDARY:</div><div class="accVal">${esc(meta.canonicalBoundary)}</div></div>
    <div class="accLine"><div class="accKey">DEPLOY:</div><div class="accVal">PUBLIC GATEWAY ONLY</div></div>
  `;
}

function initModuleModal(modules) {
  const overlay = document.getElementById("overlay");
  const mFrame = document.getElementById("mFrame");
  const mTitle = document.getElementById("mTitle");
  const mSub = document.getElementById("mSub");
  const mClose = document.getElementById("mClose");

  function escHtml(s) {
    return String(s)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  }

  function openModule(m) {
    mTitle.textContent = `${m.id} / MODULE READER`;
    mSub.textContent = m.modal.sub || "—";

    const doc = `<!doctype html><html><head><meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <style>
      body{ margin:18px; background:#000; color:#EEE; font-family:system-ui,sans-serif; line-height:1.6; }
      .hdr{ font-family:monospace; letter-spacing:.14em; text-transform:uppercase; font-size:12px; color:rgba(238,238,238,.7); }
      h1{ font-family:Georgia,serif; margin:10px 0 14px; font-size:28px; }
      .sec{ border-top:1px solid rgba(238,238,238,.18); padding-top:12px; margin-top:12px; }
      .lbl{ font-family:monospace; letter-spacing:.14em; text-transform:uppercase; font-size:12px; color:rgba(238,238,238,.7); }
      .txt{ margin-top:8px; color:rgba(238,238,238,.82); }
      .quote{ padding-left:12px; border-left:2px solid rgba(238,238,238,.18); }
      ul{ margin:8px 0 0; padding-left:18px; color:rgba(238,238,238,.82); }
    </style></head><body>
      <div class="hdr">${escHtml(m.id)} / MODULE MODAL</div>
      <h1>${escHtml(m.title)}</h1>
      <div class="sec"><div class="lbl">Purpose</div><div class="txt">${escHtml(m.modal.purpose)}</div></div>
      <div class="sec"><div class="lbl">Quote (verbatim)</div><div class="txt quote">"${escHtml(m.quote)}"</div></div>
      <div class="sec"><div class="lbl">Interpretation (labeled)</div><div class="txt">${escHtml(m.interpretation)}</div></div>
      <div class="sec"><div class="lbl">What to read next</div><div class="txt">${escHtml(m.modal.readNext)}</div></div>
      <div class="sec"><div class="lbl">Why this matters</div><div class="txt">${escHtml(m.modal.why)}</div></div>
      <div class="sec"><div class="lbl">Sources used</div><ul>${(m.modal.sources || []).map((s) => `<li>${escHtml(s)}</li>`).join("")}</ul></div>
      <div class="sec"><div class="lbl">Servant-layer reminder</div><div class="txt">Quotes are verbatim. Interpretation is labeled. Governing PDFs remain authoritative.</div></div>
    </body></html>`;

    mFrame.srcdoc = doc;
    overlay.style.display = "flex";
    mClose.focus();
  }

  function closeModal() {
    overlay.style.display = "none";
    mFrame.removeAttribute("srcdoc");
  }

  document.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-open-module]");
    if (!btn) return;
    e.preventDefault();
    const id = btn.getAttribute("data-open-module");
    const mod = modules.find((x) => x.id === id);
    if (mod) openModule(mod);
  });

  mClose.addEventListener("click", closeModal);
  overlay.addEventListener("click", (e) => { if (e.target === overlay) closeModal(); });
  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && overlay.style.display === "flex") closeModal();
  });
}

async function init() {
  try {
    const [governing, companion, modules, artifacts, readerPath, meta] = await Promise.all([
      loadJSON("data/governing.json"),
      loadJSON("data/companion.json"),
      loadJSON("data/modules.json"),
      loadJSON("data/artifacts.json"),
      loadJSON("data/reader-path.json"),
      loadJSON("data/institutional-metadata.json")
    ]);

    const availability = await buildAvailabilityMap(
      collectPdfPaths(governing, companion, modules, readerPath)
    );

    renderLedger("governingLedger", governing, availability);
    renderLedger("companionLedger", companion, availability);
    renderModulePlates(modules, availability);
    renderArtifacts(artifacts);
    renderReaderPath(readerPath, availability);
    renderFooter(meta);
    initModuleModal(modules);
  } catch (err) {
    console.error("Plate reader init failed:", err);
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init);
} else {
  init();
}

from pathlib import Path
import re, json, hashlib, yaml

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Normalize CL-EV-001 source exports into a frozen builder specification")
    parser.add_argument("--prompt-export", required=True, type=Path)
    parser.add_argument("--copy-register", required=True, type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    return parser.parse_args()


args = parse_args()
root = args.root
prompt_path = args.prompt_export
copy_path = args.copy_register
(root / "volumes/CL-EV-001").mkdir(parents=True, exist_ok=True)

prompt_text = prompt_path.read_text(encoding='utf-8-sig')
copy_text = copy_path.read_text(encoding='utf-8-sig')

page_re = re.compile(
    r'^(CL-PM-I(?P<issue_num>\d{2})-P(?P<page_num>\d)) \| (?P<issue>[^|]+?) \| (?P<title>.+?)\n'
    r'Page role: (?P<role>.+?)\n'
    r'Production intent: (?P<intent>.+?)\n'
    r'Prompt:\n(?P<prompt>.+?)\n'
    r'Negative prompt: (?P<negative>.+?)\n'
    r'Gate state: (?P<gate>.+?)\n',
    re.M | re.S,
)

copy_re = re.compile(
    r'^(CL-PM-I(?P<issue_num>\d{2})-P(?P<page_num>\d)) \| (?P<issue>[^|]+?) \| (?P<title>[^|]+?) \| (?P<role>[^|]+?) \| (?P<status>[^|]+?) \| (?P<words>\d+) words \| Copy (?P<copy>YES|NO) \| Source trace (?P<trace>[^|]+?) \| Relic (?P<relic>.+)$',
    re.M,
)
copy_index = {m.group(1): m.groupdict() for m in copy_re.finditer(copy_text)}
role_map = {
    'Encounter': 'RELIC_ENTRY',
    'Mechanism / Witness': 'WITNESS_RECORD',
    'Institution / Expansion': 'SYSTEM_TRANSLATION',
    'Residue / Turn': 'ARCHIVE_DISPOSITION',
}

issues = {}
pages = []
for m in page_re.finditer(prompt_text):
    g = m.groupdict()
    pid = m.group(1)
    c = copy_index.get(pid)
    issue_num = int(g['issue_num'])
    page_num = int(g['page_num'])
    issue_name = g['issue'].strip()
    issues.setdefault(issue_num, issue_name)
    text = ' '.join([g['intent'], g['prompt']]).lower()
    human_terms = ['human hand', 'a hand', 'person ', 'people ', 'human presence', 'human room', 'human handwriting', 'user ', 'worker']
    partial_human = any(term in text for term in human_terms)
    material_terms = []
    for term in ['ivory', 'paper', 'glass', 'steel', 'mirror', 'desk', 'interface', 'ledger', 'card', 'report', 'note']:
        if term in text:
            material_terms.append(term)
    page = {
        'page_id': pid,
        'issue_number': issue_num,
        'issue': issue_name,
        'page_number': page_num,
        'display_label': g['role'].strip(),
        'function_code': role_map[g['role'].strip()],
        'title': g['title'].strip(),
        'production_intent': g['intent'].strip(),
        'source_prompt': g['prompt'].strip(),
        'source_negative_prompt': g['negative'].strip(),
        'copy': {
            'source_document_id': '1bc1q2G0Ai7WJzB9qNsthvuSxnNfiSnbRVZ364sWsIUY',
            'copy_register_id': '1-cGDIUQmK2xsFW0u89LwInWp_GGflOBcsv5Vsyea3Xc',
            'locked': True,
            'word_count': int(c['words']) if c else None,
            'source_trace': c['trace'].strip() if c else 'UNRESOLVED',
            'relic_status': c['relic'].strip() if c else 'UNRESOLVED',
            'authoritative_text_in_image': False,
        },
        'render_overrides': {
            'human_presence': {
                'mode': 'partial_evidence' if partial_human else 'none',
                'identifiable': False,
                'cinematic': False,
                'subordinate_to_relic': True,
            },
            'material_translation_terms': sorted(set(material_terms)),
            'allow_environment': False,
            'allow_cast_shadow': False,
            'allow_transparency': False,
        },
    }
    pages.append(page)

assert len(pages) == 48, len(pages)
assert len(copy_index) == 48, len(copy_index)

source_sha_prompt = hashlib.sha256(prompt_path.read_bytes()).hexdigest()
source_sha_copy = hashlib.sha256(copy_path.read_bytes()).hexdigest()

volume = {
    'schema_version': '1.0.0',
    'volume_id': 'CL-EV-001',
    'working_id': 'CL-PM',
    'title': 'THE PYGMALION MACHINE',
    'subtitle': 'Projection, Artificial Intimacy, and the Mirror That Learned to Speak',
    'core_line': "AI is not Galatea becoming human. AI is Pygmalion’s mirror learning to speak.",
    'state': 'BUILD_VALIDATED',
    'render_authorization': {
        'status': 'NOT_APPROVED_FOR_RENDER',
        'authorized': False,
        'authorization_record': None,
    },
    'authority': {
        'canon': 'Crisis Liturgies Canon v1.1',
        'generation_standard': 'CL-GEN-STD-001 v1.0',
        'builder_amendment': 'CCR-CL-002',
        'function_palette_amendment': 'CCR-CL-003',
        'volume_ccr': 'CL-PM_CANON_CHANGE_REPORT',
    },
    'release_profile': 'crisis-liturgies-expansion-v1',
    'page_profile': {
        'name': 'expansion-volume',
        'mapping': {
            'Encounter': 'RELIC_ENTRY',
            'Mechanism / Witness': 'WITNESS_RECORD',
            'Institution / Expansion': 'SYSTEM_TRANSLATION',
            'Residue / Turn': 'ARCHIVE_DISPOSITION',
        },
    },
    'canvas': {
        'master_width': 3750,
        'master_height': 4950,
        'reader_width': 1086,
        'reader_height': 1448,
        'orientation': 'portrait',
        'background_hex': '#000000',
        'transparent_background': False,
    },
    'visual_doctrine': {
        'speaking_mirror_not_living_machine': True,
        'object_as_witness': True,
        'canvas': 'matte_black',
        'ink_family': 'metallic_silver_tonal',
        'max_foreground_coverage': 0.25,
        'authoritative_typography_stage': 'layout',
        'prohibited_canvas_terms': ['white', 'warm white', 'cream', 'ivory', 'beige', 'gray paper', 'aged paper', 'transparent'],
    },
    'issues': [{'number': n, 'title': issues[n]} for n in sorted(issues)],
    'sources': [
        {
            'name': 'CL-EV-001_48_PRODUCTION_PACKETS_VISUAL_PROMPTS',
            'provider_id': '1voVahSydR2cjws5I_s6B2pCJkMk6z-OcS7g36i7JNo4',
            'sha256': source_sha_prompt,
            'role': 'visual_prompt_source',
        },
        {
            'name': 'CL-PM_48_PAGE_COPY_REGISTER',
            'provider_id': '1-cGDIUQmK2xsFW0u89LwInWp_GGflOBcsv5Vsyea3Xc',
            'sha256': source_sha_copy,
            'role': 'copy_control_index',
        },
        {
            'name': 'CL-PM_DF_FINAL_PROSE_MANUSCRIPT',
            'provider_id': '1bc1q2G0Ai7WJzB9qNsthvuSxnNfiSnbRVZ364sWsIUY',
            'sha256': None,
            'role': 'authoritative_copy',
        },
    ],
    'pages': pages,
}

(root / 'volumes/CL-EV-001/volume.yaml').write_text(yaml.safe_dump(volume, sort_keys=False, allow_unicode=True, width=1000), encoding='utf-8')

state = {
    'volume_id': 'CL-EV-001',
    'state': 'BUILD_VALIDATED',
    'render_authorized': False,
    'blocked_on': ['APPROVED_FOR_RENDER'],
    'current_spec': 'volume.yaml',
    'last_event': 'SPEC_NORMALIZATION_AND_PREFLIGHT_PASS',
    'updated_at': '2026-08-03T07:53:00-04:00',
}
(root / 'volumes/CL-EV-001/current-state.json').write_text(json.dumps(state, indent=2) + '\n', encoding='utf-8')

events = [
    {'event': 'CCR_CL_003_ACCEPTED', 'at': '2026-08-03T07:53:00-04:00', 'state': 'SPEC_NORMALIZATION'},
    {'event': 'SPEC_NORMALIZED', 'at': '2026-08-03T07:53:00-04:00', 'pages': 48, 'state': 'BUILD_VALIDATED'},
]
(root / 'volumes/CL-EV-001/event-log.jsonl').write_text('\n'.join(json.dumps(e) for e in events) + '\n', encoding='utf-8')

print(f'parsed {len(pages)} pages across {len(issues)} issues')

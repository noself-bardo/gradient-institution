# Custody and Checksum Protocol v1.0

Every release records:

- source lineage and frozen base commit;
- manifest, file count, and byte count;
- per-file SHA-256 values;
- deterministic content-set SHA-256;
- package SHA-256;
- tests, CI, exceptions, and review state;
- repository, Drive, and Notion custody links.

Checksums describe exact bytes. Rebuilt packages receive new checksums and commit identities. Never reuse a prior checksum for reconstructed content. Stop with `CUSTODY CONTRADICTION` when an approved reference disagrees with its frozen record.

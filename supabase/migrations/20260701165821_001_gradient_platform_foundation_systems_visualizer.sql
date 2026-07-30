create schema if not exists gradient;

create or replace function gradient.set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create table if not exists gradient.departments (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Active',
  version text not null default '1.0',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  jurisdiction jsonb not null default '{}'::jsonb
);

create table if not exists gradient.standards (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Active',
  version text not null default '1.0',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  authority_layer text,
  dependencies jsonb not null default '[]'::jsonb
);

create table if not exists gradient.collections (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Draft',
  version text not null default '0.1',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text
);

create table if not exists gradient.publications (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Draft',
  version text not null default '0.1',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  collection_id uuid references gradient.collections(id) on delete set null
);

create table if not exists gradient.artifacts (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Draft',
  version text not null default '0.1',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  collection_id uuid references gradient.collections(id) on delete set null,
  publication_id uuid references gradient.publications(id) on delete set null,
  artifact_type text,
  metadata jsonb not null default '{}'::jsonb
);

create table if not exists gradient.prompt_packets (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Draft',
  version text not null default '0.1',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  artifact_id uuid references gradient.artifacts(id) on delete cascade,
  prompt_text text,
  packet_json jsonb not null default '{}'::jsonb
);

create table if not exists gradient.image_generations (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Queued',
  version text not null default '0.1',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  prompt_packet_id uuid references gradient.prompt_packets(id) on delete set null,
  generation_metadata jsonb not null default '{}'::jsonb
);

create table if not exists gradient.qc_reports (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Draft',
  version text not null default '0.1',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  artifact_id uuid references gradient.artifacts(id) on delete set null,
  asset_registry_id text,
  disposition text,
  report_json jsonb not null default '{}'::jsonb
);

create table if not exists gradient.layouts (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Draft',
  version text not null default '0.1',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  publication_id uuid references gradient.publications(id) on delete set null,
  layout_json jsonb not null default '{}'::jsonb
);

create table if not exists gradient.print_packages (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Draft',
  version text not null default '0.1',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  publication_id uuid references gradient.publications(id) on delete set null,
  package_json jsonb not null default '{}'::jsonb
);

create table if not exists gradient.archive_records (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Draft',
  version text not null default '0.1',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  source_record_id uuid,
  source_record_type text,
  archive_json jsonb not null default '{}'::jsonb
);

create table if not exists gradient.automation_jobs (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Queued',
  version text not null default '0.1',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  job_type text,
  schedule text,
  job_json jsonb not null default '{}'::jsonb
);

create table if not exists gradient.events (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Open',
  version text not null default '0.1',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  event_type text not null,
  source_record_id text,
  source_record_type text,
  prior_status text,
  new_status text,
  actor text,
  payload_json jsonb not null default '{}'::jsonb,
  downstream_actions jsonb not null default '[]'::jsonb,
  retry_count integer not null default 0,
  resolution_status text not null default 'Unresolved'
);

create table if not exists gradient.sync_records (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Pending',
  version text not null default '0.1',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  source_system text not null,
  target_system text not null,
  source_url text,
  target_url text,
  last_checked_at timestamptz,
  sync_json jsonb not null default '{}'::jsonb
);

create table if not exists gradient.platform_assets (
  id uuid primary key default gen_random_uuid(),
  registry_id text not null unique,
  title text not null,
  status text not null default 'Prototype',
  version text not null default '0.1',
  owner_department text,
  notion_url text,
  drive_url text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  notes text,
  asset_type text not null,
  asset_json jsonb not null default '{}'::jsonb
);

create index if not exists idx_gradient_artifacts_collection_id on gradient.artifacts(collection_id);
create index if not exists idx_gradient_artifacts_publication_id on gradient.artifacts(publication_id);
create index if not exists idx_gradient_prompt_packets_artifact_id on gradient.prompt_packets(artifact_id);
create index if not exists idx_gradient_image_generations_prompt_packet_id on gradient.image_generations(prompt_packet_id);
create index if not exists idx_gradient_qc_reports_artifact_id on gradient.qc_reports(artifact_id);
create index if not exists idx_gradient_layouts_publication_id on gradient.layouts(publication_id);
create index if not exists idx_gradient_print_packages_publication_id on gradient.print_packages(publication_id);
create index if not exists idx_gradient_events_source on gradient.events(source_record_type, source_record_id);
create index if not exists idx_gradient_sync_records_systems on gradient.sync_records(source_system, target_system);

alter table gradient.departments enable row level security;
alter table gradient.standards enable row level security;
alter table gradient.collections enable row level security;
alter table gradient.publications enable row level security;
alter table gradient.artifacts enable row level security;
alter table gradient.prompt_packets enable row level security;
alter table gradient.image_generations enable row level security;
alter table gradient.qc_reports enable row level security;
alter table gradient.layouts enable row level security;
alter table gradient.print_packages enable row level security;
alter table gradient.archive_records enable row level security;
alter table gradient.automation_jobs enable row level security;
alter table gradient.events enable row level security;
alter table gradient.sync_records enable row level security;
alter table gradient.platform_assets enable row level security;

do $$
declare
  table_name text;
begin
  foreach table_name in array array[
    'departments',
    'standards',
    'collections',
    'publications',
    'artifacts',
    'prompt_packets',
    'image_generations',
    'qc_reports',
    'layouts',
    'print_packages',
    'archive_records',
    'automation_jobs',
    'events',
    'sync_records',
    'platform_assets'
  ]
  loop
    execute format('drop trigger if exists set_updated_at on gradient.%I', table_name);
    execute format(
      'create trigger set_updated_at before update on gradient.%I for each row execute function gradient.set_updated_at()',
      table_name
    );
  end loop;
end;
$$;

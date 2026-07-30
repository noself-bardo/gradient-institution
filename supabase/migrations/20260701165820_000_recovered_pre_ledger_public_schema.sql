-- Recovered from the live Systems Visualizer catalog.
-- This migration preserves the historical schema as found; it does not redesign it.

create table public.projects (
  id uuid default gen_random_uuid() not null,
  user_id uuid,
  title text default 'Untitled project'::text not null,
  description text,
  created_at timestamp with time zone default now() not null,
  updated_at timestamp with time zone default now() not null,
  constraint projects_pkey primary key (id)
);

create table public.conversations (
  id uuid default gen_random_uuid() not null,
  project_id uuid not null,
  openai_conversation_id text,
  title text default 'New conversation'::text not null,
  created_at timestamp with time zone default now() not null,
  updated_at timestamp with time zone default now() not null,
  constraint conversations_pkey primary key (id)
);

create table public.messages (
  id uuid default gen_random_uuid() not null,
  conversation_id uuid not null,
  role text not null,
  content text default ''::text not null,
  openai_response_id text,
  metadata jsonb default '{}'::jsonb not null,
  created_at timestamp with time zone default now() not null,
  constraint messages_pkey primary key (id),
  constraint messages_role_check check (role = any (array['system'::text, 'user'::text, 'assistant'::text, 'tool'::text]))
);

create table public.sources (
  id uuid default gen_random_uuid() not null,
  project_id uuid not null,
  title text not null,
  source_type text not null,
  storage_bucket text,
  storage_path text,
  mime_type text,
  size_bytes bigint,
  extracted_text text,
  metadata jsonb default '{}'::jsonb not null,
  created_at timestamp with time zone default now() not null,
  constraint sources_pkey primary key (id)
);

create table public.protocols (
  id text not null,
  name text not null,
  description text,
  created_at timestamp with time zone default now() not null,
  constraint protocols_pkey primary key (id)
);

create table public.protocol_versions (
  id uuid default gen_random_uuid() not null,
  protocol_id text not null,
  version text not null,
  definition jsonb not null,
  is_active boolean default false not null,
  created_at timestamp with time zone default now() not null,
  constraint protocol_versions_pkey primary key (id),
  constraint protocol_versions_protocol_id_version_key unique (protocol_id, version)
);

create table public.protocol_runs (
  id uuid default gen_random_uuid() not null,
  project_id uuid,
  conversation_id uuid,
  protocol_version_id uuid,
  status text default 'queued'::text not null,
  input jsonb default '{}'::jsonb not null,
  step_state jsonb default '{}'::jsonb not null,
  output jsonb default '{}'::jsonb not null,
  error text,
  model text,
  openai_response_id text,
  created_at timestamp with time zone default now() not null,
  completed_at timestamp with time zone,
  constraint protocol_runs_pkey primary key (id),
  constraint protocol_runs_status_check check (status = any (array['queued'::text, 'running'::text, 'completed'::text, 'failed'::text]))
);

create table public.artifacts (
  id uuid default gen_random_uuid() not null,
  project_id uuid not null,
  protocol_run_id uuid,
  artifact_type text not null,
  title text not null,
  current_version_id uuid,
  created_at timestamp with time zone default now() not null,
  updated_at timestamp with time zone default now() not null,
  constraint artifacts_pkey primary key (id)
);

create table public.artifact_versions (
  id uuid default gen_random_uuid() not null,
  artifact_id uuid not null,
  version_number integer default 1 not null,
  content jsonb not null,
  created_at timestamp with time zone default now() not null,
  constraint artifact_versions_artifact_id_version_number_key unique (artifact_id, version_number),
  constraint artifact_versions_pkey primary key (id)
);

alter table public.conversations
  add constraint conversations_project_id_fkey
  foreign key (project_id) references public.projects(id) on delete cascade;

alter table public.messages
  add constraint messages_conversation_id_fkey
  foreign key (conversation_id) references public.conversations(id) on delete cascade;

alter table public.sources
  add constraint sources_project_id_fkey
  foreign key (project_id) references public.projects(id) on delete cascade;

alter table public.protocol_versions
  add constraint protocol_versions_protocol_id_fkey
  foreign key (protocol_id) references public.protocols(id) on delete cascade;

alter table public.protocol_runs
  add constraint protocol_runs_conversation_id_fkey
  foreign key (conversation_id) references public.conversations(id) on delete set null;

alter table public.protocol_runs
  add constraint protocol_runs_project_id_fkey
  foreign key (project_id) references public.projects(id) on delete cascade;

alter table public.protocol_runs
  add constraint protocol_runs_protocol_version_id_fkey
  foreign key (protocol_version_id) references public.protocol_versions(id) on delete set null;

alter table public.artifacts
  add constraint artifacts_project_id_fkey
  foreign key (project_id) references public.projects(id) on delete cascade;

alter table public.artifacts
  add constraint artifacts_protocol_run_id_fkey
  foreign key (protocol_run_id) references public.protocol_runs(id) on delete set null;

alter table public.artifact_versions
  add constraint artifact_versions_artifact_id_fkey
  foreign key (artifact_id) references public.artifacts(id) on delete cascade;

alter table public.projects enable row level security;
alter table public.conversations enable row level security;
alter table public.messages enable row level security;
alter table public.sources enable row level security;
alter table public.protocols enable row level security;
alter table public.protocol_versions enable row level security;
alter table public.protocol_runs enable row level security;
alter table public.artifacts enable row level security;
alter table public.artifact_versions enable row level security;

grant all on table public.projects to anon, authenticated, service_role;
grant all on table public.conversations to anon, authenticated, service_role;
grant all on table public.messages to anon, authenticated, service_role;
grant all on table public.sources to anon, authenticated, service_role;
grant all on table public.protocols to anon, authenticated, service_role;
grant all on table public.protocol_versions to anon, authenticated, service_role;
grant all on table public.protocol_runs to anon, authenticated, service_role;
grant all on table public.artifacts to anon, authenticated, service_role;
grant all on table public.artifact_versions to anon, authenticated, service_role;

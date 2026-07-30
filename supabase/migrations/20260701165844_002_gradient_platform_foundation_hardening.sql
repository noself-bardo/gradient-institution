create or replace function gradient.set_updated_at()
returns trigger
language plpgsql
set search_path = gradient, pg_temp
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

create index if not exists idx_gradient_publications_collection_id on gradient.publications(collection_id);

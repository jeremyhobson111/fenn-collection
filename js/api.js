// Shared by the phone site, GM page and TV page. The key below is the public "anon" key:
// it can only call the game's RPC functions (tables are locked, answers never leave the server).
const SB_URL = 'https://ewxioudeqpfyqdwzdtdy.supabase.co';
const SB_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV3eGlvdWRlcXBmeXFkd3pkdGR5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE1MTE0NjYsImV4cCI6MjEwNzA4NzQ2Nn0.V_Kq6ONt7l1sxblitpmZCJ9zpcJg3Ym5VZbCI6UfDAk';

async function rpc(fn, args) {
  const r = await fetch(`${SB_URL}/rest/v1/rpc/${fn}`, {
    method: 'POST',
    headers: { apikey: SB_KEY, Authorization: 'Bearer ' + SB_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify(args || {}),
  });
  if (!r.ok) throw new Error('rpc ' + fn + ' ' + r.status);
  return r.json();
}
const sleep = (ms) => new Promise((res) => setTimeout(res, ms));

const EPILOGUE = [
  'Iris Fenn crossed the Detroit River on the night of October 31, 1926.',
  'She married Daniel Lascoe and lived the rest of her life in Windsor, Ontario, as Irene Lascoe.',
  'She wrote to her sister every Halloween. Walter Pruitt hid every letter until he died. After that, her letters came back unopened. She kept writing anyway.',
  'June Fenn held a séance every Halloween for sixty years, waiting for her sister’s word.',
  'Tonight, someone finally said it.',
];

export async function divineText(text: string) {
  const res = await fetch("http://127.0.0.1:8000/divine/text", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });

  if (!res.ok) {
    throw new Error("API request failed");
  }

  return res.json();
}

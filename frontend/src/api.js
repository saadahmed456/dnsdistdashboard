export async function fetchTopQueries() {
  const response = await fetch('http://localhost:8000/api/top-queries');
  return response.json();
}

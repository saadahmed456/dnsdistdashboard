import React, { useEffect, useState } from 'react';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/top-queries')
      .then(response => response.json())
      .then(data => setData(data));
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>DNSDIST Top Queries</h1>
      {data.map((server, index) => (
        <div key={index}>
          <h2>{server.server}</h2>
          {server.error ? (
            <p style={{ color: 'red' }}>{server.error}</p>
          ) : (
            <ul>
              {server.top_queries.map((query, i) => (
                <li key={i}>{query.qname} - {query.qtype}</li>
              ))}
            </ul>
          )}
        </div>
      ))}
    </div>
  );
}

export default App;

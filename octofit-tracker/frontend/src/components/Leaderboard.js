import React, { useEffect, useState } from 'react';

  const [leaderboard, setLeaderboard] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
  useEffect(() => {
  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        setLeaderboard(data.results ? data.results : data);
      })
      .catch(err => console.error('Erro ao buscar leaderboard:', err));
  }, [endpoint]);
    fetch(endpoint)
      <h2>Leaderboard</h2>
      <ul>
        {leaderboard.map((entry, idx) => (
          <li key={entry.id || idx}>{entry.name || JSON.stringify(entry)}</li>
        ))}
      </ul>
};

export default Leaderboard;
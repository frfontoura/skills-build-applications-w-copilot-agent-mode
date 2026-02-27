import React, { useEffect, useState } from 'react';

  const [teams, setTeams] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
  useEffect(() => {
  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        setTeams(data.results ? data.results : data);
      })
      .catch(err => console.error('Erro ao buscar teams:', err));
  }, [endpoint]);
    fetch(endpoint)
      <h2>Teams</h2>
      <ul>
        {teams.map((team, idx) => (
          <li key={team.id || idx}>{team.name || JSON.stringify(team)}</li>
        ))}
      </ul>

export default Teams;
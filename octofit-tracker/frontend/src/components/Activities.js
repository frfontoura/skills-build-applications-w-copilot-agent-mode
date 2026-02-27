import React, { useEffect, useState } from 'react';

  const [activities, setActivities] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
  useEffect(() => {
  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        setActivities(data.results ? data.results : data);
      })
      .catch(err => console.error('Erro ao buscar atividades:', err));
  }, [endpoint]);
    fetch(endpoint)
      <h2>Activities</h2>
      <ul>
        {activities.map((activity, idx) => (
          <li key={activity.id || idx}>{activity.name || JSON.stringify(activity)}</li>
        ))}
      </ul>

export default Activities;
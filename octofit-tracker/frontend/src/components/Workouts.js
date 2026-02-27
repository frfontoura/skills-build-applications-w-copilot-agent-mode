import React, { useEffect, useState } from 'react';

  const [workouts, setWorkouts] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
  useEffect(() => {
  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        setWorkouts(data.results ? data.results : data);
      })
      .catch(err => console.error('Erro ao buscar workouts:', err));
  }, [endpoint]);
    fetch(endpoint)
      <h2>Workouts</h2>
      <ul>
        {workouts.map((workout, idx) => (
          <li key={workout.id || idx}>{workout.name || JSON.stringify(workout)}</li>
        ))}
      </ul>

export default Workouts;
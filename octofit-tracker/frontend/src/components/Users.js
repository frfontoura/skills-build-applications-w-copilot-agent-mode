import React, { useEffect, useState } from 'react';

  const [users, setUsers] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
  useEffect(() => {
  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        setUsers(data.results ? data.results : data);
      })
      .catch(err => console.error('Erro ao buscar users:', err));
  }, [endpoint]);
    fetch(endpoint)
      <h2>Users</h2>
      <ul>
        {users.map((user, idx) => (
          <li key={user.id || idx}>{user.name || JSON.stringify(user)}</li>
        ))}
      </ul>

export default Users;
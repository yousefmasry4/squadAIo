import React, { useState, useEffect } from "react";
import { CONFIG } from "./config";

interface State {
  firstname: string;
  lastname: string;
}

const App: React.FC = () => {
  const [users, setUsers] = useState<State[]>([]);

  useEffect(() => {
    const f = () => {
      fetch(CONFIG.API_BASE_URL)
        .then((results) => {
          return results.json();
        })
        .then((users) => {
          setUsers(users);
        });
    };
    f();
  }, []);

  const userList = users.map((user, index) => (
    <li key={index}>
      {user.lastname} {user.firstname}
    </li>
  ));

  return (
    <>
      <h3>User List</h3>
      <ul>{userList}</ul>
    </>
  );
};

export default App;

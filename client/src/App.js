import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import LoginPage from "./LoginPage";
import LoginPageAdmin from "./LoginPageAdmin";
import NewHackathonPage from "./NewHackathonPage";
import HackathonListPage from "./HackathonListPage";
import SignUpPage from "./SignUpPage";
import RegisterToHackathonPage from "./RegisterToHackathonPage";
import ViewHackathonPage from "./ViewHackathonPage";

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" exact element={<LoginPage />} />
          <Route path="/sign-up" element={<SignUpPage />} />
          <Route path="/login-admin" element={<LoginPageAdmin />} />
          <Route path="/hackathon-list" element={<HackathonListPage />} />
          <Route path="/view-hackathon" element={<ViewHackathonPage />} />
          <Route
            path="/register-to-hackathon"
            element={<RegisterToHackathonPage />}
          />
          <Route path="/new-hackathon" element={<NewHackathonPage />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;

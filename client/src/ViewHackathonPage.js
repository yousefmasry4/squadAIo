import React, { useState } from "react";
import "./ViewHackathonPage.css";
import { useLocation, useNavigate } from "react-router-dom";
import NavbarAdmin from "./NavbarAdmin";
import NavbarUser from "./NavbarUser";
import { useTranslation } from "react-i18next";

function ViewHackathonPage() {
  const location = useLocation();
  const userType = location.state.userType;
  const hackathon = location.state.hackathon;
  const navigate = useNavigate();
  const handleRegister = () => {
    // Perform login logic here
    // Assuming you have userType and credentials variables

    const id = hackathon.id; // Example user type

    // Navigate to the Hackathon List page and pass userType and credentials as state
    navigate("/register-to-hackathon", { state: { id } });
  };
  const [t, i18n] = useTranslation("global");

  // const initialFormData = {
  //   name: hackathon.name,
  //   theme: "Theme of the Hackathon",
  //   startRegistrationDate: "2024-01-01",
  //   endRegistrationDate: "2024-01-15",
  //   eventDate: "2024-02-01",
  //   challengeTitles: ["Challenge 1", "Challenge 2", "Challenge 3"],
  //   maxTeamSize: "5",
  //   maxNumberOfTeams: "20",
  // };
  console.log(userType, hackathon);
  const [registeredTeams, setRegisteredTeams] = useState([
    "Team A",
    "Team B",
    "Team C",
  ]);

  return (
    <>
      {userType === "admin" ? <NavbarAdmin /> : <NavbarUser />}
      <div className="container mt-5">
        <div className="row justify-content-center align-items-center">
          <div className="col-md-8">
            <div className="card hackathon-card">
              <div className="card-body ">
                <h2 className="card-title mb-4 text-center">
                  {hackathon.name}
                </h2>
                <p
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  className="card-text"
                >
                  <strong>{t("theme")}:</strong> {hackathon.theme}
                </p>
                <p
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  className="card-text"
                >
                  <strong>{t("period")}:</strong>{" "}
                  {hackathon.startRegistrationDate} {t("to")} {" "}
                  {hackathon.endRegistrationDate}
                </p>
                <p
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  className="card-text"
                >
                  <strong>{t("date")}:</strong> {hackathon.eventDate}
                </p>
                <p
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  className="card-text"
                >
                  <strong>{t("titles")}:</strong>{" "}
                  {hackathon.challengeTitles.join(", ")}
                </p>
                <p
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  className="card-text"
                >
                  <strong>{t("size")}:</strong> {hackathon.maxTeamSize}
                </p>
                <p
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  className="card-text"
                >
                  <strong>{t("number")}:</strong> {hackathon.maxNumberOfTeams}
                </p>
                {userType === "admin" && (
                  <div
                    style={{
                      direction: i18n.language === "en" ? "ltr" : "rtl",
                    }}
                  >
                    <hr />
                    <h4>{t("teams")}:</h4>
                    {registeredTeams.map((team, index) => (
                      <p key={index}>{team}</p>
                    ))}
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
        {userType !== "admin" && (
          <div className="row justify-content-center mt-4">
            <div className="col-md-8">
              <div className="text-center">
                <button
                  className="btn btn-primary btn-lg"
                  onClick={handleRegister}
                >
                  {t("register2")}
                </button>
              </div>
            </div>
          </div>
        )}
      </div>
    </>
  );
}

export default ViewHackathonPage;

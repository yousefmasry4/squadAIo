import React from "react";
import { Link, useNavigate } from "react-router-dom";
import img from "./MicrosoftTea22ms-image.png";
import Nav from "./NavbarLogin";
import { useTranslation } from "react-i18next";

function LoginPageAdmin() {
  const navigate = useNavigate();

  // Function to handle form submission
  const handleLogin = () => {
    // Perform login logic here
    // Assuming you have userType and credentials variables

    const userType = "admin"; // Example user type
    const credentials = { username: "admin", password: "password" }; // Example credentials

    // Navigate to the Hackathon List page and pass userType and credentials as state
    navigate("/hackathon-list", { state: { userType, credentials } });
  };

  const [t, i18n] = useTranslation("global");

  return (
    <div className="container-fluid h-100 p-0">
      <Nav />
      <div className="row justify-content-center align-items-center h-100 m-5">
        <div className="col-md-6">
          <div className="text-center">
            <img
              src={img}
              alt="Logo"
              className="img-fluid"
              style={{ height: "75vh" }}
            />
          </div>
        </div>
        <div className="col-md-6" style={{ width: "40%" }}>
          <div className="text-center">
            <h2>{t("admin-login")}</h2>
            <form onSubmit={handleLogin}>
              <div className="form-group mb-4">
                <input
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  type="text"
                  className="form-control"
                  placeholder={t("username")}
                />
              </div>
              <div className="form-group mb-4">
                <input
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  type="password"
                  className="form-control"
                  placeholder={t("password")}
                />
              </div>
              <button type="submit" className="btn btn-primary btn-block">
                {t("login")}
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default LoginPageAdmin;

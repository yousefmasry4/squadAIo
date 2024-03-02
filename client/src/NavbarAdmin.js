import React from "react";
import "./NavbarAdmin.css";
import { useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import logo from "./logo.png"

const NavbarAdmin = () => {
  const navigate = useNavigate(); // Initialize the useNavigate hook

  const handleNavigate = (pageName) => {
    // Define a function to handle navigation
    navigate(`/${pageName}`, { state: { userType: "admin" } }); // Navigate to the '/hackathons' route
  };

  const handleSignOut = () => {
    navigate("/"); // Navigate to the '/hackathons' route
  };

  const [t, i18n] = useTranslation("global");
  const handleLanguage = () => {
    i18n.changeLanguage(i18n.language === "en" ? "ar" : "en");
  };
  return (
    <nav
      className={`navbar flex-row${i18n.language === "en" ? "" : "-reverse"}`}
    >
      <div className="logo-placeholder px-5">{t("squadalo")}</div>
      <div className={`logo-placeholder p${i18n.language === "en"? "e":"s"}-5`}><img src={logo}/></div>
      <ul className="nav-menu me-auto ms-5">
        <li
          className="nav-item"
          onClick={handleNavigate.bind(null, "hackathon-list")}
        >
          {t("view-hackathon")}
        </li>
        <li
          className="nav-item"
          onClick={handleNavigate.bind(null, "new-hackathon")}
        >
          {t("add-hackathon")}
        </li>
        {/* Add onClick event to trigger navigation */}
      </ul>
      <div className="signout-button px-5">
      <button onClick={handleLanguage}>{i18n.language === "en" ? "ع": i18n.language.toUpperCase()}</button>
        <button style={{ marginLeft: "10px" }} onClick={handleSignOut}>
        {t("signout")}        </button>
      </div>
    </nav>
  );
};

export default NavbarAdmin;

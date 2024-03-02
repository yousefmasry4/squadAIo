import React from "react";
import { useNavigate } from "react-router-dom"; // Import the useNavigate hook
import "./NavbarUser.css";
import { useTranslation } from "react-i18next";
import logo from "./logo.png"
const NavbarUser = () => {
  const navigate = useNavigate(); // Initialize the useNavigate hook

  const handleNavigate = () => {
    // Define a function to handle navigation
    navigate("/hackathon-list", { state: { userType: "user" } }); // Navigate to the '/hackathons' route
  };

  const handleSignOut = () => {
    navigate("/"); // Navigate to the '/hackathons' route
  };

  const [t, i18n] = useTranslation("global");
  const handleLanguage = () => {
    i18n.changeLanguage(i18n.language === "en" ? "ar" : "en");
  };
  return (
    <nav className={`navbar flex-row${i18n.language === "en"? "":"-reverse"}`}>
      <div className="logo-placeholder px-5">{t("squadalo")}</div>
      <div className={`logo-placeholder p${i18n.language === "en"? "e":"s"}-5`}><img src={logo}/></div>
      <ul className={`nav-menu m${i18n.language === "en"? "e":"s"}-auto ms-5`}>
        <li className="nav-item" onClick={handleNavigate}>
          {t("view-hackathon")}
        </li>
        {/* Add onClick event to trigger navigation */}
      </ul>
      <div className="signout-button px-5">
      <button onClick={handleLanguage}>{i18n.language === "en" ? "ع": i18n.language.toUpperCase()}</button>
        <button style={{ marginLeft: '10px' }} onClick={handleSignOut}>{t("signout")}</button>
      </div>
    </nav>
  );
};

export default NavbarUser;

import React from "react";
import "./NavbarLogin.css";
import { useTranslation } from "react-i18next";
import logo from "./logo.png";

const NavbarLogin = () => {
  const [t, i18n] = useTranslation("global");
  const handleLanguage = () => {
    i18n.changeLanguage(i18n.language === "en" ? "ar" : "en");
  };
  return (
    <nav
      className={`navbar flex-row${i18n.language === "en" ? "" : "-reverse"}`}
    >
      <div className="logo-placeholder px-5 py-2">{t("squadalo")}</div>
      <div
        className={`logo-placeholder p${i18n.language === "en" ? "e" : "s"}-5`}
      >
        <img src={logo} />
      </div>
      <ul className="nav-menu me-auto ms-5">
        <li className="nav-item" />
      </ul>
      <div className="signout-button px-5">
        <button onClick={handleLanguage}>
          {i18n.language === "en" ? "ع" : i18n.language.toUpperCase()}
        </button>
      </div>
    </nav>
  );
};

export default NavbarLogin;

import React, { useState } from "react";
import "./NewHackathonPage.css";
import NavbarAdmin from "./NavbarAdmin";
import { useTranslation } from "react-i18next";

const NewHackathonPage = () => {
  const [formData, setFormData] = useState({
    name: "",
    theme: "",
    startRegistrationDate: "",
    endRegistrationDate: "",
    eventDate: "",
    challengeTitles: [],
    maxTeamSize: "",
    maxNumberOfTeams: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    if (name === "challengeTitles" && value === ",") {
      setFormData({
        ...formData,
        [name]: [name].concat(value),
      });
    } else {
      setFormData({
        ...formData,
        [name]: value,
      });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // You can handle form submission here, such as sending the data to an API or saving it in a database
    console.log(formData);
    // Reset the form after submission
    setFormData({
      name: "",
      theme: "",
      startRegistrationDate: "",
      endRegistrationDate: "",
      eventDate: "",
      challengeTitles: [],
      maxTeamSize: "",
      maxNumberOfTeams: "",
    });
  };
  const [t, i18n] = useTranslation("global");

  return (
    <>
      <NavbarAdmin />
      <div
        className="container-fluid h-100 bg-light pt-5"
        style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
      >
        <div className="row justify-content-center align-items-center h-100">
          <div className="col-md-6">
            <div className="card p-4 shadow">
              <h1 className="text-center mb-4">{t("add-hackathon")}</h1>
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label className="form-label">{t("name")}:</label>
                  <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    className="form-control"
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">{t("theme")}:</label>
                  <input
                    type="text"
                    name="theme"
                    value={formData.theme}
                    onChange={handleChange}
                    className="form-control"
                  />
                </div>
                <div className="row mb-3">
                  <div className="col">
                    <label className="form-label">
                    {t("start-date")}:
                    </label>
                    <input
                      type="date"
                      name="startRegistrationDate"
                      value={formData.startRegistrationDate}
                      onChange={handleChange}
                      className="form-control"
                    />
                  </div>
                  <div className="col">
                    <label className="form-label">{t("end-date")}:</label>
                    <input
                      type="date"
                      name="endRegistrationDate"
                      value={formData.endRegistrationDate}
                      onChange={handleChange}
                      className="form-control"
                    />
                  </div>
                </div>
                <div className="mb-3">
                  <label className="form-label">{t("date")}:</label>
                  <input
                    type="date"
                    name="eventDate"
                    value={formData.eventDate}
                    onChange={handleChange}
                    className="form-control"
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">{t("commas")}:</label>
                  <input
                    type="text"
                    name="challengeTitles"
                    value={formData.challengeTitles}
                    onChange={handleChange}
                    className="form-control"
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">{t("size")}:</label>
                  <input
                    type="number"
                    name="maxTeamSize"
                    value={formData.maxTeamSize}
                    onChange={handleChange}
                    className="form-control"
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">{t("number")}:</label>
                  <input
                    type="number"
                    name="maxNumberOfTeams"
                    value={formData.maxNumberOfTeams}
                    onChange={handleChange}
                    className="form-control"
                  />
                </div>
                <div className="text-center">
                  <button type="submit" className="btn btn-primary">
                  {t("submit")}
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default NewHackathonPage;

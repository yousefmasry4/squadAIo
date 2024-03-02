import React, { useState } from "react";
import img from "./MicrosoftTea22ms-image.png";
import Nav from "./NavbarLogin";
import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";

function SignUpPage() {
  const [formData, setFormData] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    reEnterPassword: "",
    birthday: "",
    gender: "",
  });

  const handleChange = (e) => {
    console.log(formData);
    const { name, value } = e.target;
    setFormData((prevFormData) => ({
      ...prevFormData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission here, e.g., send data to server
    console.log(formData);
  };
  const [t, i18n] = useTranslation("global");

  return (
    <div className="container-fluid h-100 bg-light p-0">
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
        <div className="col-md-6" style={{ width: "35%" }}>
          <div className="text-center">
            <h2>{t("register")}</h2>
            <p className="mb-4">{t("register-free")}</p>
            <form onSubmit={handleSubmit}>
              <div className="form-group mb-4">
                <input
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  type="text"
                  className="form-control"
                  placeholder={t("first-name")}
                  name="firstName"
                  value={formData.firstName}
                  onChange={handleChange}
                />
              </div>
              <div className="form-group mb-4">
                <input
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  type="text"
                  className="form-control"
                  placeholder={t("last-name")}
                  name="lastName"
                  value={formData.lastName}
                  onChange={handleChange}
                />
              </div>
              <div className="form-group mb-4">
                <input
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  type="email"
                  className="form-control"
                  placeholder={t("email")}
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                />
              </div>
              <div className="form-group mb-4">
                <input
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  type="password"
                  className="form-control"
                  placeholder={t("password")}
                  name="password"
                  value={formData.password}
                  onChange={handleChange}
                />
              </div>
              <div className="form-group mb-4">
                <input
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  type="password"
                  className="form-control"
                  placeholder={t("password2")}
                  name="reEnterPassword"
                  value={formData.reEnterPassword}
                  onChange={handleChange}
                />
              </div>
              <div className="form-group mb-4">
                <input
                  type="date"
                  className="form-control"
                  name="birthday"
                  value={formData.birthday}
                  onChange={handleChange}
                />
              </div>
              <div className="form-group mb-4">
                <select
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                  className="form-control"
                  name="gender"
                  value={formData.gender}
                  onChange={handleChange}
                >
                  <option value="" disabled>
                    {t("gender")}
                  </option>
                  <option value="Male">{t("male")}</option>
                  <option value="Female">{t("female")}</option>
                </select>
              </div>
              <Link to="/" className="btn btn-primary btn-block mx-2">
                {t("register")}
              </Link>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SignUpPage;

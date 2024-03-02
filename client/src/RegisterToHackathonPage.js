import React, { useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import NavbarUser from "./NavbarUser";
import { useTranslation } from "react-i18next";

const RegisterToHackathonPage = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const id = location.state.id;
  console.log(id);
  const [formData, setFormData] = useState({
    teamName: "",
    selectedChallenges: [],
    members: [{ title: "", name: "", id: "", email: "", mobile: "" }],
  });
  const [t, i18n] = useTranslation("global");
  const [challengesDropdownOpen, setChallengesDropdownOpen] = useState(false);

  const handleChange = (e, index, type) => {
    const { name, value } = e.target;
    const updatedMembers = [...formData.members];
    if (type === "member") {
      updatedMembers[index] = { ...updatedMembers[index], [name]: value };
      setFormData({ ...formData, members: updatedMembers });
    } else if (type === "challenge") {
      setFormData({
        ...formData,
        [name]: value.split(",").map((item) => item.trim()),
      });
      setChallengesDropdownOpen(false); // Close dropdown when a challenge is selected
    } else {
      setFormData({ ...formData, [name]: value });
    }
  };

  const addMember = () => {
    if (formData.members.length < 5) {
      setFormData({
        ...formData,
        members: [
          ...formData.members,
          { title: "", name: "", id: "", email: "", mobile: "" },
        ],
      });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // You can handle form submission here, such as sending the data to an API or saving it in a database
    console.log(formData);
    // Reset the form after submission
    setFormData({
      teamName: "",
      selectedChallenges: [],
      members: [{ title: "", name: "", id: "", email: "", mobile: "" }],
    });
    navigate("/hackathon-list", { state: { userType: "asf" } });
  };

  return (
    <>
      <NavbarUser />

      <div className="container-fluid h-100 bg-light">
        <div className="row justify-content-center align-items-center h-100">
          <div className="col-md-6">
            <div className="card p-4 shadow">
              <h1 className="text-center mb-4">{t("register2")}</h1>
              <form onSubmit={handleSubmit}>
                <div
                  className="mb-3"
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                >
                  <label className="form-label">{t("team")}:</label>
                  <input
                    type="text"
                    name="teamName"
                    value={formData.teamName}
                    onChange={(e) => handleChange(e, null, "team")}
                    className="form-control"
                  />
                </div>
                <div
                  className="mb-3"
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                >
                  <label className="form-label">{t("challenge")}:</label>
                  <div
                    className={`dropdown${
                      challengesDropdownOpen ? " show" : ""
                    }`}
                  >
                    <button
                      className="btn btn-secondary dropdown-toggle w-100"
                      type="button"
                      onClick={() =>
                        setChallengesDropdownOpen(!challengesDropdownOpen)
                      }
                    >
                      {formData.selectedChallenges.length > 0
                        ? formData.selectedChallenges.join(", ")
                        : t("challenge2")}
                    </button>
                    <div
                      className={`dropdown-menu${
                        challengesDropdownOpen ? " show" : ""
                      }`}
                      aria-labelledby="dropdownMenuButton"
                    >
                      {["AI", "Robotics", "Embedded", "FrontEnd"].map(
                        (challenge, index) => (
                          <button
                            key={index}
                            className={`dropdown-item`}
                            type="button"
                            onClick={() =>
                              handleChange(
                                {
                                  target: {
                                    name: "selectedChallenges",
                                    value: challenge,
                                  },
                                },
                                null,
                                "challenge"
                              )
                            }
                          >
                            {challenge}
                          </button>
                        )
                      )}
                    </div>
                  </div>
                </div>
                <div
                  className="mb-3"
                  style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
                >
                  {formData.members.map((member, index) => (
                    <div key={index}>
                      <h3 className="mb-2">
                        {t("member")} {(index + 1).toLocaleString(i18n.language === "en"? "en-US": "ar-SA")}
                      </h3>
                      <input
                        style={{
                          direction: i18n.language === "en" ? "ltr" : "rtl",
                        }}
                        type="text"
                        name="title"
                        value={member.title}
                        onChange={(e) => handleChange(e, index, "member")}
                        className="form-control mb-2"
                        placeholder={t("title")}
                      />
                      <input
                        style={{
                          direction: i18n.language === "en" ? "ltr" : "rtl",
                        }}
                        type="text"
                        name="name"
                        value={member.name}
                        onChange={(e) => handleChange(e, index, "member")}
                        className="form-control mb-2"
                        placeholder={t("name")}
                      />
                      <input
                        style={{
                          direction: i18n.language === "en" ? "ltr" : "rtl",
                        }}
                        type="text"
                        name="id"
                        value={member.id}
                        onChange={(e) => handleChange(e, index, "member")}
                        className="form-control mb-2"
                        placeholder={t("id")}
                      />
                      <input
                        style={{
                          direction: i18n.language === "en" ? "ltr" : "rtl",
                        }}
                        type="email"
                        name="email"
                        value={member.email}
                        onChange={(e) => handleChange(e, index, "member")}
                        className="form-control mb-2"
                        placeholder={t("email")}
                      />
                      <input
                        style={{
                          direction: i18n.language === "en" ? "ltr" : "rtl",
                        }}
                        type="text"
                        name="mobile"
                        value={member.mobile}
                        onChange={(e) => handleChange(e, index, "member")}
                        className="form-control mb-3"
                        placeholder={t("mobile")}
                      />
                    </div>
                  ))}
                  {formData.members.length < 5 && (
                    <button
                      type="button"
                      className="btn btn-secondary mb-3"
                      onClick={addMember}
                    >
                      {t("add-member")}
                    </button>
                  )}
                </div>
                <div className="text-center">
                  <button type="submit" className="btn btn-primary">
                    Submit
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

export default RegisterToHackathonPage;

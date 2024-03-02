import React from "react";
import img from "./image.png";
import Nav from "./NavbarLogin";
import { Link, useNavigate } from "react-router-dom";
import { useTranslation } from "react-i18next";
import axios from "axios"

function LoginPage() {
  const navigate = useNavigate();
  const [t, i18n] = useTranslation("global");
  const [username, setUsername] = React.useState("");
  const [password, setPassword] = React.useState("");
  // Function to handle form submission
  const handleLogin = async () => {
    // Perform login logic here
    // Assuming you have userType and credentials variables

    
      var data = JSON.stringify({
        "password": "1234567",
        "username": "string2"
      });
      
      var config = {
        method: 'post',
        url: 'http://localhost:5050/api/auth/login',
        headers: { 
          'Content-Type': 'application/json',
          // origin 
          'Accept': '*/*',
          'Access-Control-Allow-Origin': '*'
        },
        data : data
      };
      
      axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
      
    const userType = "competitor"; // Example user type
    const credentials = { username: "admin", password: "password" }; // Example credentials


    // Navigate to the Hackathon List page and pass userType and credentials as state
    navigate("/hackathon-list", { state: { userType, credentials } });
  };
  return (
    <div style={{height: "100vh"}} className="container-fluid d-flex flex-column p-0">
      <Nav />
      <div className="row justify-content-center align-items-center h-100 m-5">
        <div className="col-md-7">
          <div className="text-center">
            <img
              src={img}
              alt="Logo"
              className="img-fluid"
              // style={{ height: "75vh" }}
            />
          </div>
        </div>
        <div className="col-md-5" style={{ width: "40%" }}>
          <div className="text-center">
            <h2>{t("login")}</h2>
            <form onSubmit={handleLogin}>
              <div className="form-group mb-4">
                <input
                style={{direction: i18n.language === "en"? "ltr": "rtl"}}
                  type="text"
                  className="form-control"
                  placeholder={t("username")}
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                />
              </div>
              <div className="form-group mb-4">
                <input
                style={{direction: i18n.language === "en"? "ltr": "rtl"}}
                  type="password"
                  className="form-control"
                  placeholder={t("password")}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  
                />
              </div>
              <button type="submit" className="btn btn-primary btn-block">
              {t("log-in")}
              </button>
              <Link to="/sign-up" className="btn btn-secondary btn-block mx-2">
              {t("register")}
              </Link>
            </form>
          </div>
          <div className="text-center justify-content-end">
        <Link to="/login-admin" className="btn btn-link">
        {t("admin-login")}
        </Link>
      </div>
        </div>
      </div>
      
    </div>
  );
}

export default LoginPage;

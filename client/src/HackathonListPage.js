import React, { useState, useEffect } from "react";
import HackathonCard from "./HackathonCard";
import { Container, Row } from "react-bootstrap";
import { useLocation, useNavigate } from "react-router-dom";
import NavbarUser from "./NavbarUser";
import NavbarAdmin from "./NavbarAdmin";
import { useTranslation } from "react-i18next";

function HackathonListPage() {
  const [hackathons, setHackathons] = useState([]);
  const [displayCount, setDisplayCount] = useState(9);
  const location = useLocation();
  const userType = location.state.userType;
  const navigate = useNavigate();

  const [t, i18n] = useTranslation("global")

  // Mock hackathon data
  useEffect(() => {
    // Load initial hackathons
    loadHackathons();
  }, []);

  // Function to load hackathons
  const loadHackathons = () => {
    // Replace this with your API call to fetch hackathon data
    // For demonstration, using a mock array of hackathons
    const mockHackathons = [
      {
        id: 1,
        name: "Hackathon Name",
        theme: "Theme of the Hackathon",
        startRegistrationDate: "2024-01-01",
        endRegistrationDate: "2024-01-15",
        eventDate: "2024-02-01",
        challengeTitles: ["Challenge 1", "Challenge 2", "Challenge 6"],
        maxTeamSize: "5",
        maxNumberOfTeams: "20",
      },
      { id: 2, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 3, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 4, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 5, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 6, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 7, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 8, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 9, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 10, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 11, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 12, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 13, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 14, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 15, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 16, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 17, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 18, name: "Hackathon 2", eventDate: "2024-03-15" },
      { id: 19, name: "Hackathon 255", eventDate: "2024-03-15" },
      // Add more hackathon data as needed
    ];

    setHackathons(mockHackathons);
  };

  // Function to handle card click
  const handleCardClick = (hackathon) => {
    // Navigate to ViewHackathonPage passing the hackathon details
    navigate(`/view-hackathon`, { state: { userType, hackathon } });
  };

  return (
    <>
      {userType === "admin" ? <NavbarAdmin /> : <NavbarUser />}

      <Container className="mt-5">
        <h1 className="text-center fw-bold mb-4">{t('hackathon-list')}</h1>
        <Row xs={1} md={3} className="g-4">
          {hackathons.slice(0, displayCount).map((hackathon) => (
            <HackathonCard
              key={hackathon.id}
              hackathon={hackathon}
              onView={() => handleCardClick(hackathon)}
            />
          ))}
        </Row>
        <div className="text-center mt-3">
          <button
            className="btn btn-primary"
            onClick={() => setDisplayCount((prevCount) => prevCount + 9)}
          >
            {t("load")}
          </button>
        </div>
      </Container>
    </>
  );
}

export default HackathonListPage;

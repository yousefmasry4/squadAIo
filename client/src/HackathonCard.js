import React from "react";
import { Card } from "react-bootstrap";
import { useTranslation } from "react-i18next";

function HackathonCard({ hackathon, onView }) {
  const [t, i18n] = useTranslation("global");

  return (
    <div className="col-md-4 mb-4" style={{ height: "30vh" }}>
      <Card
        className="bg-light"
        onClick={() => onView(hackathon.id)}
        style={{ cursor: "pointer", height: "100%" }}
      >
        <Card.Body
          style={{ direction: i18n.language === "en" ? "ltr" : "rtl" }}
        >
          <Card.Title className="font-weight-bold">{hackathon.name}</Card.Title>
          <Card.Text className="font-weight-light">
            {t("date")}: {hackathon.eventDate}
          </Card.Text>
        </Card.Body>
      </Card>
    </div>
  );
}

export default HackathonCard;

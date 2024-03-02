// index.js
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import "bootstrap/dist/css/bootstrap.min.css"; // Add this line to import Bootstrap CSS
import reportWebVitals from "./reportWebVitals";

import global_en from "./translations/en/global.json";
import global_ar from "./translations/ar/global.json";
import i18next from "i18next";
import { I18nextProvider } from "react-i18next";

i18next.init({
  interpolation: { escapeValue: false },
  lng: "en",
  resources: {
    en: {
      global: global_en,
    },
    ar: {
      global: global_ar,
    },
  },
});

const link = document.createElement("link");
link.rel = "stylesheet";
link.href =
  "https://fonts.googleapis.com/css2?family=Readex+Pro:wght@160..700&display=swap"; // Example URL, replace with your chosen fonts

// Append the link element to the document head
document.head.appendChild(link);

ReactDOM.render(
  <React.StrictMode>
    <I18nextProvider i18n={i18next}>
      <App />
    </I18nextProvider>
  </React.StrictMode>,
  document.getElementById("root")
);

reportWebVitals();

import React from "react";
import ReactDOM from "react-dom/client";

// import { App } from "./app";
// import 'bootstrap/dist/css/bootstrap.min.css';
// import "./assets/css/bootstrap.min.css";

//Bootstrap
import "bootstrap/dist/css/bootstrap.min.css";

//Font Awesome
import "./assets/plugins/fontawesome/css/fontawesome.min.css";
import "./assets/plugins/fontawesome/css/all.min.css";

//CSS
import "./assets/css/style.css";

import Approuter from "./approuter";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <>
    <Approuter />
  </>
);

import React from "react";
// import config from "config";

import { Route, BrowserRouter as Router } from "react-router-dom";
import Header from "./components/header";
import Home from "./components/home";
import Footer from "./components/footer";

const AppContainer = function () {
  return (
    // <Router basename={`${config.publicPath}`}>
    <Router basename="/reactjs">
      <>
        <Route render={(props) => <Header {...props} />} />
        
          {/* home */}
          <Route exact path="/" component={Home} />
        

        <Route render={(props) => <Footer {...props} />} />
      </>
    </Router>
  );
};

export default AppContainer;

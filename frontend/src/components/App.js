import React, { Component } from "react";
import { render } from "react-dom";
import { createRoot } from "react-dom/client";
import HomePage from "./HomePage";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <HomePage />
      </div>
    );
  }
}

const myApp = document.getElementById("app");
const root = createRoot(myApp);
root.render(<App tab="home" />);

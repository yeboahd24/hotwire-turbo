// This is the scss entry file
// import "../styles/stimulus_basic.scss";
// import "@hotwired/turbo";

// import { Application } from "@hotwired/stimulus";
// import CounterController from "../controllers/counter_controller";
// import { definitionsFromContext } from "@hotwired/stimulus-webpack-helpers";


// window.Stimulus = Application.start();
// window.Stimulus.register("counter", CounterController);
// const context = require.context("../controllers", true, /\.js$/);
// window.Stimulus.load(definitionsFromContext(context));

// This is the scss entry file
import "../styles/stimulus_basic.scss";
import "@hotwired/turbo";
import { Application } from "@hotwired/stimulus";
import { definitionsFromContext } from "@hotwired/stimulus-webpack-helpers";

window.Stimulus = Application.start();
const context = require.context("../controllers", true, /\.js$/);
window.Stimulus.load(definitionsFromContext(context));
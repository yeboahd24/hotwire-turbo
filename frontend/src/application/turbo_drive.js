// This is the scss entry file
import "../styles/turbo_drive.scss";
import "../styles/turbo_frame.scss";
import "@hotwired/turbo";
// update
window.document.addEventListener("DOMContentLoaded", function() {
    window.console.log("dom ready");
});
document.addEventListener('turbo:load', function() {
    console.log('turbo:load');
});

document.addEventListener("turbo:before-cache", function() {
    console.log('turbo:before-cache');
    const form = document.querySelector('form');
    if (form) {
        form.reset();
    }
});

document.addEventListener('turbo:before-render', () => {
    document.querySelector('#weatherwidget-io-js').remove();
});

document.addEventListener("turbo:submit-start", function({ target }) {
    console.log('turbo:submit-start');
    console.log(target);
});
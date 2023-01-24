const styleSheet = document.getElementById("dark-mode-styles");
const button = document.getElementById("dark-mode-button");
const placeholder = document.getElementById("dark-mode-button-placeholder");

const DARK_MODE = "dark";
const LIGHT_MODE = "light";

const currentMode = sessionStorage.getItem("mode") || LIGHT_MODE;

function setMode(mode) {
  styleSheet.disabled = mode === LIGHT_MODE;
  button.textContent = mode === DARK_MODE ? "Light Mode" : "Dark Mode";
  sessionStorage.setItem("mode", mode);
}

setMode(currentMode);

button.addEventListener("click", () => {
  const mode = styleSheet.disabled ? DARK_MODE : LIGHT_MODE;
  setMode(mode);
});

placeholder.appendChild(button);

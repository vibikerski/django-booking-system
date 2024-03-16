const roomId = document.currentScript.dataset.roomid;

$.ajax({
  url: `/rooms/${roomId}/taken`,
  method: "GET",
  success: (data) => {
    takenDates = data.dates;
  },
  error: (error) => {
    console.error("Error fetching taken dates:", error);
  },
});

const dateInput1 = document.getElementById("start-date");
const dateInput2 = document.getElementById("end-date");
let takenDates = [];

const validateDateInput = (dateInput) => {
  const dateValue = new Date(dateInput.value);
  let validityMessage = "";

  if (dateValue < new Date()) {
    validityMessage = "Please enter a date in the future.";
  } else if (takenDates.includes(dateValue.toISOString().split("T")[0])) {
    validityMessage = "Sorry, that date is not available for the selected room.";
  }

  dateInput.setCustomValidity(validityMessage);
  dateInput.classList.toggle("is-invalid", !dateInput.checkValidity());
};

dateInput1.addEventListener("input", () => validateDateInput(dateInput1));
dateInput2.addEventListener("input", () => validateDateInput(dateInput2));

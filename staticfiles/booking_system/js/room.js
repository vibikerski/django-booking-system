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


const validateDateRange = (startDateInput, endDateInput) => {
  const startDateValue = new Date(startDateInput.value);
  const endDateValue = new Date(endDateInput.value);

  if (endDateValue <= startDateValue) {
    endDateInput.setCustomValidity("End date must be after the start date.");
    endDateInput.classList.add("is-invalid");
  } else {
    endDateInput.setCustomValidity("");
    endDateInput.classList.remove("is-invalid");
  }
}

const validateDate = (dateInput) => {
  validateDateInput(dateInput);
  validateDateRange(dateInput1, dateInput2);
}

dateInput1.addEventListener("input", () => validateDate);
dateInput2.addEventListener("input", () => validateDate);

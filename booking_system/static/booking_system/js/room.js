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

const validateEndDate = () => {
  const startDateValue = new Date(dateInput1.value);
  const endDateValue = new Date(dateInput2.value);

  if (endDateValue <= startDateValue) {
    dateInput2.setCustomValidity("End date must be after the start date.");
    dateInput2.classList.add("is-invalid");
  } else {
    dateInput2.setCustomValidity("");
    dateInput2.classList.remove("is-invalid");
  }
};

dateInput1.addEventListener("input", () => {
  validateDateInput(dateInput1);
  validateEndDate();
});
dateInput2.addEventListener("input", () => {
  validateDateInput(dateInput2);
  validateEndDate();
});

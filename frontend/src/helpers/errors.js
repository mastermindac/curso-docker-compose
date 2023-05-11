/**
 * Returns the input string with the first letter capitalized.
 * 
 * @param {string} word 
 * @returns {string}
 */
function capitalizeFirstLetter(word) {
  return word.charAt(0).toUpperCase() + word.slice(1);
}

/**
 * Converts validation errors returned by the backend API to a human readable
 * string.
 * 
 * @param {Object} errors Validation errors returned by the backend.
 * @returns {string}
 */
function humanReadableError(errors) {
  const emptyStringErrors = [
    "Missing data for required field.",
    "Shorter than minimum length 1.",
    "Field may not be null.",
  ];

  const [firstWrongField, [firstError]] = Object.entries(errors)[0];

  if (emptyStringErrors.includes(firstError)) {
    return `"${capitalizeFirstLetter(firstWrongField)}" is required.`
  }

  return firstError;
}

function httpErrorMessage(e) {
  return e.response?.data?.message ?? e.message ?? "Unknown Error";
}

export {
  humanReadableError,
  capitalizeFirstLetter,
  httpErrorMessage,
}

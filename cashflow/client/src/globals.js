export const BASE_URL =
  process.env.VUE_APP_ENV === 'production'
    ? `${window.location.origin}`
    : 'http://localhost:8000';

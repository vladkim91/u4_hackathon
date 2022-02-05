export const BASE_URL =
  process.env.VUE_APP_ENV === 'production'
    ? `${window.location.origin}/api`
    : 'http://localhost:8000/api';

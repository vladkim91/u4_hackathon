import axios from 'axios';
import { BASE_URL } from '../globals';

const Client = axios.create({
  baseURL: BASE_URL,
  auth: {
    username: process.env.VUE_APP_DB_USERNAME,
    password: process.env.VUE_APP_DB_PASSWORD
  }
});

export default Client;

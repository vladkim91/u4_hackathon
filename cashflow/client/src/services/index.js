import axios from 'axios';
import { BASE_URL } from '../globals';

const Client = axios.create({ baseURL: BASE_URL });

export default Client;

import Client from './';

export const userLogin = async (userInfo) => {
  const result = await Client.post('/profile', userInfo);
  return result.data;
};

export const registerUser = async (userInfo) => {
  const result = await Client.post('/profile/create', userInfo);
  return result.data;
};

import Client from './';

export const registerUser = async (userInfo) => {
  const result = await Client.post('/profile/create', userInfo);
  return result.data;
};

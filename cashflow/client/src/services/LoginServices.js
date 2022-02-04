import Client from './';

export const userLogin = async (userInfo) => {
  const result = await Client.post('/profile/login', userInfo);
  return result.data;
};

export const getUserProfile = async (userId) => {
  const result = await Client.post('/profile', {
    user: userId
  });

  return result.data;
};

export const registerUser = async (userInfo) => {
  const result = await Client.post('/profile/create', userInfo);
  return result.data;
};

from linear import EnvelopeLinearCQN
from cnn import EnvelopeCnnCQN

def get_new_model(name, state_size, action_size, reward_size):
	if name == 'linear':
		return EnvelopeLinearCQN(state_size, action_size, reward_size)
	if name == 'cnn':
		return EnvelopeCnnCQN(state_size, action_size, reward_size)
	else:
		print "model %s doesn't exist."%(name)
		return None
class CustomStopper:
	def __init__(self, patience=10, min_delta=0.002, min_iter=40):
		self.patience = patience
		self.min_delta = min_delta
		self.min_iter = min_iter
		self.best_score = None
		self.iter_since_best = 0

	def __call__(self, optim_result):
		current_iter = len(optim_result.x_iters)
		current_best = optim_result.fun
		score = -current_best

		if current_iter < self.min_iter:
			if self.best_score is None or score > self.best_score:
				self.best_score = score

			# Debug
			print(
				f"Iter: {current_iter} (Exploration),\n"
				f"Score: {score:.4f}, Best: {self.best_score:.4f}"
			)
            
			return False
		else:
			if self.best_score is None or score > self.best_score + self.min_delta:
				self.best_score = score
				self.iter_since_best = 0
			else:
				self.iter_since_best += 1

			# Debug
			print(
				f"Iter: {current_iter},\n"
				f"Score: {score:.4f},\n"
				f"Best: {self.best_score:.4f},\n"
				f"Seit letzter Verbesserung: {self.iter_since_best}"
			)

			return self.iter_since_best >= self.patience
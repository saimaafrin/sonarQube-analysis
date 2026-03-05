def render(pieces, style):
	"""
	Input pieces and a style, render the pieces to the corresponding style.
	"""
	if style == "chess":
		return render_chess(pieces)
	elif style == "chessboard":
		return render_chessboard(pieces)
	elif style == "chessboard_with_pieces":
		return render_chessboard_with_pieces(pieces)
	elif style == "chessboard_with_pieces_and_coordinates":
		return render_chessboard_with_pieces_and_coordinates(pieces)
	elif style == "chessboard_with_pieces_and_coordinates_and_highlights":
		return render_chessboard_with_pieces_and_coordinates_and_highlights(pieces)
	elif style == "chessboard_with_pieces_and_coordinates_and_highlights_and_moves":
		return render_chessboard_with_pieces_and_coordinates_and_highlights_and_moves(pieces)
	elif style == "chessboard_with_pieces_and_coordinates_and_highlights_and_moves_and_checks":
		return render_chessboard_with_pieces_and_coordinates_and_highlights_and_moves_and_checks(pieces)
	elif style == "chessboard_with_pieces_and_coordinates_and_highlights_and_moves_and_checks_and_checkmate":
		return render_chessboard_with_pieces_and_coordinates_and_highlights_and_moves_and_checks_and_checkmate(pieces)
	elif style == "chessboard_with_pieces_and_coordinates_and_highlights_and_moves_and_checks_and_checkmate_and_promotion":
		return render_chessboard_with_pieces_and_coordinates_and_highlights_and_moves_and_checks_and_checkmate_and_promotion(pieces)
	elif style == "chessboard_with_pieces_and_coordinates_and_highlights_and_moves
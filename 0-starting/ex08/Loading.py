import time


def ft_tqdm(lst: range) -> None:
    """
    Function immitates the original tqdm function in rendering a progress bar.

        Parameters:
                lst: The range of numbers defined
    """
    length = len(lst)
    t_start = time.time()
    for i in lst:
        yield i
        t_elapsed = time.time() - t_start
        completion = min(i / length, 1.0)
        progress_bar = ("|["
                        + "=" * round(completion * 50)
                        + ">" + " " * (50 - round(completion * 50))
                        + "]|")
        # the end="" argument in the print function is used to specify what
        # character or string should be printed at the end. A newline (\n) is
        # printed by default.
        print(
            f"\r{100 * completion:3.0f}%"
            f"{progress_bar} "
            f"{i}/{length} "
            f"[{t_elapsed:.2f}s]",
            end=""
        )


# import shutil


# def ft_tqdm(lst: range) -> None:
#     length = len(lst)
#     t_start = time.time()

#     w_terminal = shutil.get_terminal_size().columns

#     for i in lst:
#         yield i
#         t_elapsed = time.time() - t_start
#         bar_length = w_terminal - 30
#         completion = min(i / length, 1.0)
#         progress_bar = ("|["
#                         + "=" * round(completion * bar_length)
#                         + ">"
#                         + " " * (bar_length - round(completion * bar_length))
#                         + "]|")
#         print(
#             f"\r{100 * completion:3.0f}%"
#             f"{progress_bar} "
#             f"{i}/{length} "
#             f"[{t_elapsed:.2f}s]",
#             end=""
#         )

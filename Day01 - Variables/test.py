# # def SeatingStudents(arr):
# #     K = arr[0]
# #     taken = arr[1:]
# #     rows = int(K / 2)
# #     s = []
# #     x = 0
# #
# #
# #
# #     for i in range(rows):
# #         s.append([])
# #         for j in range(2):
# #             if ((x + 1) in taken):
# #                 seat_taken = True
# #             else:
# #                 seat_taken = False
# #             s[i].append(str(seat_taken))
# #             x += 1
# #
# #     seating = 0
# #     for i in range(rows - 1):
# #         if ((s[i][0] == str(False)) and (s[i][1] == str(False))):
# #             seating += 1
# #
# #         if ((s[i][0] == str(False)) and (s[i + 1][0] == str(False))):
# #             seating += 1
# #
# #         if ((s[i][1] == str(False)) and (s[i + 1][1] == str(False))):
# #             seating += 1
# #     if ((s[rows - 1][0] == str(False)) and (s[rows - 1][1] == str(False))):
# #         seating += 1
# #
# #     return seating
# #
# # print(SeatingStudents([12, 2, 6, 7, 11]))
# # print(SeatingStudents([6, 4]))
# # print(SeatingStudents([8, 1, 8]))
#
# def max_area_histogram(histogram):
#     # This function calculates maximum
#     # rectangular area under given
#     # histogram with n bars
#
#     # Create an empty stack. The stack
#     # holds indexes of histogram[] list.
#     # The bars stored in the stack are
#     # always in increasing order of
#     # their heights.
#     stack = list()
#
#     max_area = 0  # Initialize max area
#
#     # Run through all bars of
#     # given histogram
#     index = 0
#     while index < len(histogram):
#
#         # If this bar is higher
#         # than the bar on top
#         # stack, push it to stack
#
#         if (not stack) or (histogram[stack[-1]] <= histogram[index]):
#             stack.append(index)
#             index += 1
#
#         # If this bar is lower than top of stack,
#         # then calculate area of rectangle with
#         # stack top as the smallest (or minimum
#         # height) bar.'i' is 'right index' for
#         # the top and element before top in stack
#         # is 'left index'
#         else:
#             # pop the top
#             top_of_stack = stack.pop()
#
#             # Calculate the area with
#             # histogram[top_of_stack] stack
#             # as smallest bar
#             area = (histogram[top_of_stack] *
#                     ((index - stack[-1] - 1)
#                      if stack else index))
#
#             # update max area, if needed
#             max_area = max(max_area, area)
#
#     # Now pop the remaining bars from
#     # stack and calculate area with
#     # every popped bar as the smallest bar
#     while stack:
#         # pop the top
#         top_of_stack = stack.pop()
#
#         # Calculate the area with
#         # histogram[top_of_stack]
#         # stack as smallest bar
#         area = (histogram[top_of_stack] *
#                 ((index - stack[-1] - 1)
#                  if stack else index))
#
#         # update max area, if needed
#         max_area = max(max_area, area)
#
#     # Return maximum area under
#     # the given histogram
#     return max_area
#
#
# # Driver Code
# hist = [6, 3, 1, 4, 12, 4]
# print("Maximum area is",
#       max_area_histogram(hist))
#
#
# def HistogramArea(arr):
#     # initalise empty list, max area and index
#     stack = list()
#     area = 0
#     index = 0
#
#     # run through all bars in graph
#
#     while index < len(arr):
#
#         if (not stack) or (arr[stack[-1]] <= arr[index]):
#             stack.append(index)
#             index += 1
#
#         else:
#             top = stack.pop()
#
#             c_area = (arr[top] * ((index - stack[-1] - 1)
#                                   if stack else index))
#
#     while stack:
#         top = stack.pop()
#
#         c_area = (arr[top] * ((index - stack[-1] - 1)
#                               if stack else index))
#
#     # update if necc
#     area = max(area, c_area)
#
#     return area
#
#     # return arr
#
#
# # keep this function call here
# print(HistogramArea(input()))


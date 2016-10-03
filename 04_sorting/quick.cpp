#include <iostream>
#include <cstddef>
#include <vector>
#include <utility>

/*
int partition(std::vector<int> A, size_t l, size_t r) {
  int x = A[r];
  int i = l - 1;
  for (size_t j = l; j < r; ++j) {
    if (A[j] <= x) {
      i++;
      int tmp = A[j];
      A[j] = A[i];
      A[i] = tmp;
    }
  }
  int tmp = A[i + 1];
  A[i + 1] = A[r];
  A[r] = tmp;
  return i + 1;
}

// sorting a vector of pairs
struct sort_pred {
  bool operator()(const std::pair<int,int> &left, const std::pair<int,int> &right) {
    return left.first < right.first;
  }
};


*/

int main() {
  size_t n;
  size_t m;

  // read n, m
  std::cin >> n >> m;

  std::vector<int> ls(n);
  std::vector<int> rs(n);
  int l;
  int r;
  // read segments
  for (size_t i = 0; i < n; ++i) {
    std::cin >> l >> r;
    ls[i] = l;
    rs[i] = r;
  }
  
  std::vector<int> P(m);
  int pt;

  // read points
  for (size_t i = 0; i < m; ++i) {
    std::cin >> pt;
    P[i] = pt;
  }

  int counter;
  // count for each point
  for (size_t i = 0; i < m ; ++i) {
    counter = 0;
    for (size_t j = 0; j < n; ++j) {
      if ((P[i] >= ls[j]) && (P[i] <= rs[j])) {
	counter = counter + 1;
      }
    }
    std::cout << counter << ' ';
  }
  std::cout << std::endl;

  /*
  // read segment into vector of pairs
  std::vector<std::pair <int,int> > S(n);
  int l;
  int r;
  std::pair<int,int> seg;
  for (size_t i = 0; i < n; ++i) {
    std::cin >> l >> r;
    seg.first = l;
    seg.second = r;
    S[i] = seg;
  }

  std::vector<int> P(m);
  int pt;

  // read points
  for (size_t i = 0; i < m; ++i) {
    std::cin >> pt;
    P[i] = pt;
  }

  std::sort(S.begin(), S.end(), sort_pred()); // sort it

  std::vector<int> ls(n);
  std::vector<int> rs(n);

  for (size_t i = 0; i < n; ++i) {
    ls[i] = S[i].first;
    rs[i] = S[i].second;
  }
  
  int inf = 50001;
  ls.push_back(inf);
  rs.push_back(inf);

  for (size_t i = 0; i < m; ++i) {
    std::vector<int> new_ls(ls);

    new_ls[new_ls.size() - 1] = P[i];
    int idx = partition(new_ls, 0, new_ls.size() - 1);

    if (idx == 0) {
      std::cout << 0 << ' ';
      continue;
    }
    int counter = idx;
    for (size_t j = 0; j < idx; ++j) {
      if (rs[j] < P[i]) {
	counter--;
      }
    }
    std::cout << counter << ' ';
  }
  std::cout << std::endl;
  */

  return 0;
}

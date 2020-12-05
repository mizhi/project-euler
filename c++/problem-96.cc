#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <sstream>

// stl libs
#include <algorithm>
#include <iterator>
#include <set>
#include <vector>
#include <queue>

using namespace std;

// represents 3x3 portion of board.
class SudokuChunk
{
private:
  int nums[9];

  set<int> candidates[9];

public:
  SudokuChunk()
  {
    for (int i = 0; i < 9; i++) {
      nums[i] = 0;
    }
  }

  virtual ~SudokuChunk()
  {
  }

  SudokuChunk(const SudokuChunk& sc)
  {
    for (int i = 0; i < 9; i++) {
      this->nums[i] = sc.nums[i];
      
      this->candidates[i].clear();
      copy(sc.candidates[i].begin(), sc.candidates[i].end(),
	   insert_iterator<set<int> >(this->candidates[i], 
				      this->candidates[i].begin()));
    }
  }

  // returns reference to number at r,c.  Can
  // be used in assignment
  int& num_at(int r, int c)
  {
    return nums[r * 3 + c];
  }

  set<int>& candidates_at(int r, int c)
  {
    return this->candidates[r * 3 + c];
  }

  SudokuChunk& operator=(const SudokuChunk& sc)
  {
    for (int i = 0; i < 9; i++) {
      this->nums[i] = sc.nums[i];
      
      this->candidates[i].clear();
      copy(sc.candidates[i].begin(), sc.candidates[i].end(),
	   insert_iterator<set<int> >(this->candidates[i], this->candidates[i].begin()));
    }
    return *this;
  }

  int num_blank() const
  {
    int num = 0;
    for (int i = 0; i < 9; i++) {
      if (this->nums[i] == 0) {
	num++;
      }
    }
    return num;
  }
  
  int num_candidates() const
  {
    int count = 0;
    for (int i = 0; i < 9; i++) {
      count += this->candidates[i].size();
    }
    return count;
  }


  void generate_candidates()
  {
    // first, get a set with all the numbers.
    set<int> cs;
    for (int i = 1; i <= 9; i++) {
      cs.insert(cs.end(), i);
    }

    // then take out the numbers that appear in the grid
    for (int i = 0; i < 9; i++) {
      cs.erase(this->nums[i]);
    }

    // copy these candidates to each position.  This takes care of
    // candidates for this chunk
    for (int i = 0; i < 9; i++) {
      this->candidates[i].clear();
      if (this->nums[i] == 0) {
	copy(cs.begin(), cs.end(),
	     insert_iterator<set<int> >(this->candidates[i], 
					this->candidates[i].begin()));
      }
    }
  }
};

class SudokuBoard
{
private:
  SudokuChunk chunks[9];

  SudokuChunk& chunk_at(int r, int c)
  {
    return chunks[r * 3 + c];
  }

public:
  SudokuBoard()
  {    
  }

  virtual ~SudokuBoard()
  {
  }

  SudokuBoard(const SudokuBoard &sb)
  {
    for (int i = 0; i < 9; i++) {
      this->chunks[i] = sb.chunks[i];
    }
  }

  int& num_at(int r, int c)
  {
    return chunk_at(floor(r/3),floor(c/3)).num_at(r % 3, c % 3);
  }

  set<int>& candidates_at(int r, int c)
  {
    return chunk_at(floor(r/3),floor(c/3)).candidates_at(r % 3, c % 3);
  }

  int num_blank() const
  {
    int count = 0;
    for (int i = 0; i < 9; i++) {
      count += this->chunks[i].num_blank();
    }
    return count;
  }

  int num_candidates() const
  {
    int count = 0;
    for (int i = 0; i < 9; i++) {
      count += this->chunks[i].num_candidates();
    }

    return count;
  }

  void generate_candidates()
  {
    // generate candidates for each subchunk first.
    for (int i = 0; i < 9; i++) {
      this->chunks[i].generate_candidates();
    }

    // refine each candidate by row and col possibilities
    for (int r = 0; r < 9; r++) {
      // first, figure out what we have in the row nums
      set<int> row_nums;
      for (int c = 0; c < 9; c++) {
	row_nums.insert(row_nums.end(), this->num_at(r,c));
      }

      // then, for each candidate, remove those numbers that appear.
      // basically, we take the set_intersection of both sets 
      // and remove them from the candidate list.
      for (int c = 0; c < 9; c++) {
	set<int> remove_nums;
	set_intersection(this->candidates_at(r,c).begin(), this->candidates_at(r,c).end(),
			 row_nums.begin(), row_nums.end(),
			 insert_iterator<set<int> >(remove_nums, remove_nums.begin()));

	for (set<int>::iterator i = remove_nums.begin();
	     i != remove_nums.end(); i++) {
	  this->candidates_at(r,c).erase(*i);
	}						     
      }
    }

    // refine each candidate by row and col possibilities
    for (int c = 0; c < 9; c++) {
      // first, figure out what we have in the row nums
      set<int> col_nums;
      for (int r = 0; r < 9; r++) {
	col_nums.insert(col_nums.end(), this->num_at(r,c));
      }

      // then, for each candidate, remove those numbers that appear.
      // basically, we take the set_intersection of both sets 
      // and remove them from the candidate list.
      for (int r = 0; r < 9; r++) {
	set<int> remove_nums;
	set_intersection(this->candidates_at(r,c).begin(), this->candidates_at(r,c).end(),
			 col_nums.begin(), col_nums.end(),
			 insert_iterator<set<int> >(remove_nums, remove_nums.begin()));

	for (set<int>::iterator i = remove_nums.begin();
	     i != remove_nums.end(); i++) {
	  this->candidates_at(r,c).erase(*i);
	}						     
      }
    }
  }


  int top_left_3num()
  {
    return (this->num_at(0,0) * 100) + (this->num_at(0,1) * 10) + (this->num_at(0,2));
  }

  friend istream& operator>>(istream& is, SudokuBoard& sb);
  friend ostream& operator<<(ostream& os, SudokuBoard& sb);
};

istream& operator>>(istream& is, SudokuBoard& sb)
{
  int board_row = 0;

  string tag;
  getline(is, tag);
  cout << tag << endl;

  while (is && board_row < 9) {
    string gline;
    getline(is, gline);

    for (int i = 0; i < 9; i++) {
      char c = gline[i];
      int n = static_cast<int>(c) - static_cast<int>('0');
      sb.num_at(board_row,i) = n;
    }
    board_row++;
  }

  return is;
}

ostream& operator<<(ostream& os, SudokuBoard& sb)
{
  int chunk_row = 0;
  int chunk_col = 0;
  int board_row = 0;
  int board_col = 0;

  while (os && board_row < 3) {
    os << sb.chunk_at(board_row, board_col).num_at(chunk_row, chunk_col);
    chunk_col++;
    if (chunk_col == 3) {
      chunk_col = 0;
      board_col++;
      os << " ";
    }

    if (board_col == 3) {
      board_col = 0;
      chunk_row++;
      os << endl;
    }

    if (chunk_row == 3) {
      chunk_row = 0;
      board_row++;
      os << endl;
    }      
  }
  
  return os;
}

typedef pair<int,pair<int,int> > cand_type;
typedef priority_queue<cand_type,vector<cand_type>,greater<cand_type> > cand_order_type;


bool solve_board(SudokuBoard sb, SudokuBoard& sol);
bool solve_board(SudokuBoard sb, SudokuBoard& sol)
{
  sb.generate_candidates();

  if (sb.num_candidates() == 0) {
    return false;
  }

  // first, find all spots that have only one candidate.  This keeps us from needlessly
  // entering into the expensive triple loop below.
  int r = 0;
  int c = 0;
  while (r < 9 && c < 9) {
    int num_cans = sb.candidates_at(r,c).size();      
    if (num_cans == 1) {
      for (set<int>::iterator j = sb.candidates_at(r,c).begin(); j != sb.candidates_at(r,c).end(); j++) {
	sb.num_at(r,c) = *j;
      }
      sb.generate_candidates();
      c = 0;
      r = 0;
    } else {
      c++;
      if (c == 9) {
	c = 0;
	r++;
      }
    }    
  }

  // number of blank spaces is 0, so this board is solved.
  if (sb.num_blank() == 0) {
    sol = sb;
    return true;
  }

  for (int r = 0; r < 9; r++) {
    for (int c = 0; c < 9; c++) {
      if (sb.num_at(r,c) == 0) {
	int num_cans = sb.candidates_at(r,c).size();      
	set<int> cans(sb.candidates_at(r,c));
	for (set<int>::iterator i = cans.begin(); i != cans.end(); i++) {
	  sb.num_at(r,c) = *i;
	  if (solve_board(sb, sol)) {
	    return true;
	  }
	}
	return false;
      }
    }
  }
  return false;
}

int main(int argc, char **argv)
{
  ifstream ifs(argv[1]);

  int sum = 0;
  while (ifs) {
    SudokuBoard sb, sol;
    if (!(ifs >> sb)) {
      break;
    } 

    if (solve_board(sb, sol)) {
      cout << "Solution: " << endl << sol << endl;
      cout << sol.top_left_3num() << endl;

      cout << "Prev sum: " << sum << endl;
      sum += sol.top_left_3num();
    } else {
      cout << "No solution." << endl;
    }
  }

  ifs.close();


  cout << "Final sum: " << sum << endl;



  return 0;
}

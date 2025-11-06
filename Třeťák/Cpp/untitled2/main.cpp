#include <iostream>
#include <string>
#include <vector>
#include <iomanip>

class Movie {
private:
    std::string title;
    std::string director;

    class Rating {
    private:
        std::string user;
        int score;
        std::string comment;
    public:
        Rating(const std::string& user, int score, const std::string& comment)
            : user(user), score(score), comment(comment) {}

        int getScore() const { return score; }

        void print() const {
            std::cout << "  Uzivatelske jmeno: " << user << std::endl;
            std::cout << "  Skore: " << score << std::endl;
            std::cout << "  Komentar: " << comment << std::endl;
        }

        friend void printMovieDetails(const Movie& m);
    };

    std::vector<Rating> ratings;

public:
    Movie(const std::string& title, const std::string& director)
        : title(title), director(director) {}

    void addRating(const std::string& user, int score, const std::string& comment) {
        if (score < 1) score = 1;
        if (score > 10) score = 10;
        ratings.emplace_back(user, score, comment);
    }

    double getAverageRating() const {
        if (ratings.empty()) return 0.0;
        double sum = 0.0;
        for (const auto& r : ratings) {
            sum += r.getScore();
        }
        return sum / ratings.size();
    }

    friend void printMovieDetails(const Movie& m);
};

void printMovieDetails(const Movie& m) {
    std::cout << "Nazev filmu: " << m.title << std::endl;
    std::cout << "Reziser: " << m.director << std::endl;
    std::cout << "Prumerne hodnoceni: " << std::fixed << std::setprecision(2) << m.getAverageRating() << std::endl;
    std::cout << "Seznam hodnoceni:" << std::endl;
    if (m.ratings.empty()) {
        std::cout << "  Zadna hodnoceni nejsou k dispozici." << std::endl;
    } else {
        for (const auto& rating : m.ratings) {
            std::cout << "--------------------" << std::endl;
            rating.print();
        }
        std::cout << "--------------------" << std::endl;
    }
}

int main() {
    Movie film("Pelisky", "Jan Hrebejk");
    film.addRating("Petr", 9, "Vyborna komedie!");
    film.addRating("Anna", 8, "Moc se mi libilo.");
    film.addRating("Josef", 7, "Dobre, ale mohl byt lepsi scenar.");

    printMovieDetails(film);

    return 0;
}